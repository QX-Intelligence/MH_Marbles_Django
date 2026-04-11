from .models import Company


class CompanyService:

    @staticmethod
    def get_all_companies():
        return Company.objects.all()

    @staticmethod
    def get_company(company_id):
        return Company.objects.get(id=company_id)

    @staticmethod
    def create_company(data):
        return Company.objects.create(**data)

    @staticmethod
    def update_company(company, data):

        for key, value in data.items():
            setattr(company, key, value)

        company.save()

        return company

    @staticmethod
    def delete_company(company):
        company.delete()