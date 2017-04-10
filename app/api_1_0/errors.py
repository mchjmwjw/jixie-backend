@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json