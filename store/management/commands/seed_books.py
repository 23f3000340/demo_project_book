from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed the database with demo Book entries'

    def handle(self, *args, **options):
        from store.models import Book

        created = 0
        media_files = [
            'books/files/free_book_1.pdf',
            'books/files/free_book_2.pdf',
        ]

        for i in range(1, 11):
            title = f"Demo Book {i}"
            if not Book.objects.filter(title=title).exists():
                b = Book.objects.create(
                    title=title,
                    author=f"Author {i}",
                    price=0.00 if i <= 2 else 9.99 + i,
                    stock=5 + i,
                    description=("This is a demo book used to populate the catalog for development "
                                 "and UI testing."),
                )
                # attach free file to first two demo books
                if i <= len(media_files):
                    path = media_files[i-1]
                    # set path directly (file already present in MEDIA_ROOT)
                    b.file = path
                    b.save()
                created += 1

        self.stdout.write(self.style.SUCCESS(f'Created {created} demo books'))
