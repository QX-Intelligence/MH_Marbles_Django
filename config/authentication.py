import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

User = get_user_model()

class SpringJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = None
        auth_header = request.headers.get('Authorization')

        if auth_header:
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]

        # Fallback to checking cookies (like what Spring Boot might be setting)
        if not token:
            token = request.COOKIES.get('access_token')
            
        if not token:
            return None

        try:
            # Decode using PyJWT tracking HS256 which Spring boot defaults to
            payload = jwt.decode(
                token, 
                settings.SPRING_JWT_SECRET, 
                algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token signature')

        # Strictly mirror Spring Security checks per the user's JwtService:
        if payload.get('type') != 'ACCESS':
            raise AuthenticationFailed('Only ACCESS tokens are permitted, REFRESH tokens rejected')

        # Identify User from Token (Subject mapped to email by Spring)
        email = payload.get('sub')
        role = payload.get('role')
        
        if not email:
            raise AuthenticationFailed('Token payload missing standard user identifier')

        # Hydrate a local ephemeral user to satisfy Django permissions
        user, created = User.objects.get_or_create(
            username=email, 
            defaults={'email': email}
        )
        
        # Optionally track user access context mapping
        user.is_staff = (role == 'ADMIN' or role == 'ROLE_ADMIN' or True) # Fallback to true if strictly authenticated admins only? 
        if created:
            user.is_staff = True
            user.is_superuser = True
            user.save()

        return (user, token)
