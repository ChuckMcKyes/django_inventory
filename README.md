# Django Inventory

Django Inventory website, Chuck McKyes<br>
<br>
v0.1.0 November 2021<br>
<br>
Copyright (C) 2021 Chuck McKyes</br>
<br>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
<br><br>
There are too many files in /www/static to put on github. The ones missing
here are for the admin part of the Django site. If you want to try this website
then follow the instructions on docs.djangoproject.com, in particular
using "python3 manage.py collectstatic" to transfer static files to your localhost
location. In this particular setup.py, the location is /var/www/static/ and the location
for photos is /var/www/media/.
<br>https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/
<br>https://docs.djangoproject.com/en/3.2/howto/deployment/
<br>
Also, sudo chown www-data:www-data db.sqlite3 and
<br>sudo chown www-data:www-data django_inventory  (the root directory)
in order to run it on localhost.
<br><br>
The default login is 'admin' with password 'adminpassword'.
