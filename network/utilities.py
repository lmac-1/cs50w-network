def get_previous_url(page):
    if page.has_previous(): 
        previous_url = f'?page={page.previous_page_number()}'
    else: 
        previous_url = ''
    return previous_url

def get_next_url(page):
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''
    return next_url