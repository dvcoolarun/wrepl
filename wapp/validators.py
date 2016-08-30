import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
	ext = os.path.splitext(value.name)[1] # returns path + filename
	valid_extensions = ['.doc', '.docx']
	if not ext.lower() in valid_extensions:
		raise ValidationError('Unsupported file extension')