# Online reservation system - raport pracy
## Przygotowanie
### Środowisko
---
### Tutoriale i potrzebna wiedza
#### Django Polls App Tutorial
Aby dobrze zapoznać się z frameworkiem wykonano [cały tutorial do Django](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)  
Tutorial obejmował następujące tematy:
- utworzenie projektu, developement server
- utworzenie aplikacji
- utworzenie widoku
- utworzenie bazy danych
- utworzenie modelu, używanie modelu 
- formularze
- testy

Repozytorium z wykonanym tutorialem znajduje się na [repozytorium](https://github.com/Arvi-beep-boop/django-tutorial)

## Przebieg pracy nad projektem
Stworzenie diagramu relacji obiektów - koncept aplikacji  
<img src=relations.jpg alt=calendar width="400" height=300/>

- utworzenie projektu i aplikacji
- dodanie modelu adresu i danych kontaktowych
- dodanie modelu Firmy, usługodawcy
- dodanie modelu usługi
- dodanie modelu rezerwacji

Kod jednego z modelów (usługi) wygląda następująco:
```python
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    duration = models.DurationField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
``` 
Każda usługa ma swoją nazwę, pole tekstowe na opcjonalny opis, cenę, czas trwania oraz jako ForeignKey - firmę, usługodawcę danej usługi.

- dodanie widoków stron z rodzajami usług, firmami oraz poszczególnymi usługami
```python
class CategoryView(generic.ListView):
    template_name = "reservation_system/category.html"
    context_object_name = "category_list"
    def get_queryset(self):
        return Category.objects.all()
```

- dodanie kalendarza: pip install django-formset
### Struktura strony
http://127.0.0.1:8000/reservation_system/reservation/ - kalendarz  
http://127.0.0.1:8000/reservation_system/category/ - kategorie usług  
http://127.0.0.1:8000/reservation_system/1/company/ - lista firm oferujących usługę danego typu   
http://127.0.0.1:8000/reservation_system/1/service - lista usług oferowanych przez daną firmę


### Napotkane problemy
#### Nieprawidłowe wyświetlanie się kalendarza
<img src=image.png alt=calendar width="500" height=500/>

Nieprawidłowe wyświetlanie kalendarza wynikało z braku załadowania styli i js z biblioteki bootstrap.  
Przy rozwiązywaniu problemu korzystano z dokumentacji:
- [django-formset](https://django-formset.fly.dev/)
- [django-bootstrap](https://django-bootstrap-v5.readthedocs.io/en/latest/quickstart.html)
#### Odebranie sygnały naciśnięcia przycisku
Problem nie został rozwiązany
### Możliwe usprawnienia
1) **Eksportowanie umówionej wizyty do kalendarza**  
Możliwość dodania umówionej wizyty do kalendarza, np. kalendarza Google, była by dużym usprawnieniem i wygodą dla użytkowników - dobrze jest mieć wszystkie wizyty/rezerwacje/wydarzenia w jednym kalendarzu.  
2) **Dodanie systemu opinii, recenzji danej usługi lub firmy**  
Taki system pozwoliłby użytkownikom na skuteczniejsze znalezienie usługi dla siebie. Funkcjonalność zapewniłaby duży komfort korzystania z aplikacji.
3) **Usprawnienia wizualne**  
Wizualna odsłona mogłaby pomóc użytkownikowi w nawigowaniu, poruszaniu się po aplikacji. Z aplikacji, które dobrze wyglądają i dbają o pozytywny UX lepiej się korzysta.