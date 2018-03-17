from modeltranslation.translator import register, TranslationOptions
from .models import Member


@register(Member)
class MemberTranslationOptions(TranslationOptions):
    fields = ('names', 'father_last_name', 'mother_last_name', 'gender', 'birth_day', 'nationality', 'marital_status', 'document_type', 'document_id', 'email', 'person_type', 'dependent_of', 'kinship', 'picture', 'status', 'member_number', 'disabilities', 'cane_number', 'academic_level', 'currently_works', 'ocupation', 'where_work', 'observations', 'is_mother',)
