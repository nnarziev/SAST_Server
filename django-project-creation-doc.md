<b>Steps (django) project creation -> release</b><br>
1. Create a project<br>
2. Create a new module (files & terminal):<br>
	i.	run: <code>python manage.py startapp [module name]</code><br>
	ii.	add [module name] into the array inside the file <i>"settings.py"</i> inside the main module folder<br>
	iii.	inside [module name] folder, create an <i>"urls.py"</i> file<br>
	iv.	create <code>"urlpatterns = []"</code> variable inside the newly created <i>"urls.py"</i> file<br>
	v.	include the "[module name].urls" inside the main module's <i>"urls.py"</i> file<br>
	vi.	run: <code>python manage.py makemigrations</code><br>
	vii.	run: <code>python manage.py migrate</code><br>
3. Create a virtual environment (terminal):<br>
	i.	<code>python -m pip install virtualenv</code><br>
	ii.	<code>cd [project folder]</code><br>
	iii.	<code>virtualenv venv</code><br>
	iv.	Windows:	<code>venv/Scripts/activate.bat</code><br>
		Linux/Mac:	<code>source venv/bin/activate</code><br>
		-> also link project to venv (environment) from IDE settings<br>
	v.	<code>pip install -r requirements.txt</code><br>
	(vi).	regularly run: <code>pip freeze >> requirements.txt</code><br>
4. Change line <code>"Debug=True"</code> -> <code>"Debug=False"</code> inside the <i>"settings.py"</i> file<br>
5. Add server hostname to <code>"ALLOWED_HOSTS=[]"</code> array inside <i>"settings.py"</i> file<br>
6. Release the django project on a hosting website