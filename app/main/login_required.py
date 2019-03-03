def login_required(func):
    def do_wrapper():
        if current_user:
            func()
        else:
            redirect(url_for('auth.login'))
    return do_wrapper
