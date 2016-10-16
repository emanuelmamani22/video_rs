from django import template 
 
register = template.Library()

@register.filter(name='cortar')
def cortar(value):
	a = 0
	b= ''
	if len(value) > 21:
		for x in value:
			a = a + 1
			b = b + x
			if a == 21:
				break
	else:
		return value
	b = b + '...'
	return b