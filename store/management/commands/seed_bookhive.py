from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Book, Category
from django.core.files.base import ContentFile
import random


class Command(BaseCommand):
    help = 'Seed database with categories and sample books for BookHive'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            ('Fiction', 'fiction'),
            ('Non-Fiction', 'non-fiction'),
            ('Science', 'science'),
            ('Technology', 'technology'),
            ('History', 'history'),
            ('Biography', 'biography'),
            ('Self-Help', 'self-help'),
            ('Programming', 'programming'),
        ]
        
        categories = []
        for name, slug in categories_data:
            cat, created = Category.objects.get_or_create(name=name, slug=slug)
            categories.append(cat)
            if created:
                self.stdout.write(f"Created category: {name}")
        
        # Sample book data
        books_data = [
            ("The Great Algorithm", "Ada Lovelace", "A fascinating journey through the world of algorithms and computation.", 'free'),
            ("Python for Everyone", "Guido van Rossum", "Learn Python programming from the ground up.", 'free'),
            ("Data Science Handbook", "Marie Curie", "Complete guide to data science and machine learning.", 'restricted'),
            ("Web Development Mastery", "Tim Berners-Lee", "Master modern web development with this comprehensive guide.", 'free'),
            ("AI and Machine Learning", "Alan Turing", "Understanding artificial intelligence and its applications.", 'restricted'),
            ("Cloud Computing Essentials", "Grace Hopper", "Everything you need to know about cloud infrastructure.", 'free'),
            ("Cybersecurity Fundamentals", "Dorothy Vaughan", "Protect systems and data from digital attacks.", 'restricted'),
            ("The DevOps Handbook", "Katherine Johnson", "Best practices for DevOps culture and automation.", 'free'),
            ("Mobile App Development", "Steve Jobs", "Build amazing mobile applications for iOS and Android.", 'restricted'),
            ("Database Design Principles", "Edgar Codd", "Master database design and SQL queries.", 'free'),
            ("Software Architecture", "Martin Fowler", "Patterns and practices for scalable systems.", 'restricted'),
            ("Agile Methodology", "Kent Beck", "Transform your development process with Agile.", 'free'),
            ("Digital Marketing Guide", "Seth Godin", "Effective strategies for online marketing.", 'free'),
            ("Blockchain Basics", "Satoshi Nakamoto", "Understanding blockchain technology and cryptocurrencies.", 'restricted'),
            ("UI/UX Design Principles", "Don Norman", "Creating delightful user experiences.", 'free'),
            ("Network Engineering", "Vint Cerf", "Build and maintain robust computer networks.", 'restricted'),
            ("Game Development", "Shigeru Miyamoto", "Create engaging games from concept to launch.", 'free'),
            ("Data Structures", "Donald Knuth", "Essential data structures and algorithms.", 'restricted'),
            ("Linux Administration", "Linus Torvalds", "Master Linux server management.", 'free'),
            ("Clean Code", "Robert Martin", "Writing maintainable and elegant code.", 'restricted'),
        ]
        
        created_count = 0
        for title, author, desc, access_type in books_data:
            if not Book.objects.filter(title=title).exists():
                # Create a minimal PDF placeholder
                pdf_content = f"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj\n3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R/Resources<<>>>>endobj\ntrailer<</Root 1 0 R>>\n%%EOF"
                
                book = Book.objects.create(
                    title=title,
                    author=author,
                    description=desc,
                    category=random.choice(categories),
                    access_type=access_type,
                    downloads=random.randint(0, 150),
                )
                
                # Save PDF
                book.pdf.save(f"{title.replace(' ', '_').lower()}.pdf", ContentFile(pdf_content.encode()), save=True)
                created_count += 1
                
        self.stdout.write(self.style.SUCCESS(f'Created {created_count} books'))
        
        # Create demo users
        if not User.objects.filter(username='demouser').exists():
            User.objects.create_user('demouser', 'demo@example.com', 'demo1234')
            self.stdout.write(self.style.SUCCESS('Created demo user: demouser / demo1234'))
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
            self.stdout.write(self.style.SUCCESS('Created admin user: admin / admin1234'))
