# online-reservation
Zainstaluj niezbędne biblioteki i frameworki:
- [django](https://docs.djangoproject.com/en/5.0/topics/install/)
- [django-forms](https://django-formset.readthedocs.io/en/latest/installation.html)

Aby uruchomić projekt w folderze `online_reservation` uruchom komendę
`python .\manage.py runserver`

Uruchom wyświetlony w konsoli link - do adresu dopisz odpowiednio:

- `/reservation_system/category/` - wyświetlone zostaną kategorie usług, które można wybrać

Po wybraniu usługi następuje przekierowanie na stronę
- `/reservation_system/<id_kategorii>/company/`- lista firm oferujących usługę danego typu

Następnie po wybraniu firmy nastąpi przekierowanie na stronę
- `/reservation_system/1/service` - lista usług oferowanych przez daną firmę

Dodatkowo do podstawowego linku można dopisać:
`/reservation_system/reservation/` - wyświetlony zostanie kalendarz, niestety nie udało się wprowadzić pełnej funkcjonalności systemu z kalendarzem.

Do systemu można dodać również więcej kategorii usług, firm czy usług jakie są oferowane przez daną firmę. Aby to zrobić do linku dopisz `/admin`
*login*: admin  
*hasło*: admin