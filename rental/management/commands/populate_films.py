from django.core.management.base import BaseCommand
from rental.models import Film
from datetime import date

class Command(BaseCommand):
    help = 'Load sample Pinoy films into the database'

    def handle(self, *args, **kwargs):
        films_data = [
            {"title": "Himala", "genre": "Drama", "synopsis": "A woman claims to have witnessed a miracle in a poor rural village.", "release_date": date(1982, 12, 25)},
            {"title": "Ang Larawan", "genre": "Musical Drama", "synopsis": "Two sisters struggle to maintain their dignity amid financial difficulties.", "release_date": date(2017, 12, 25)},
            {"title": "Oro, Plata, Mata", "genre": "War Drama", "synopsis": "The lives of two wealthy families change drastically during World War II.", "release_date": date(1982, 1, 1)},
            {"title": "Dekada '70", "genre": "Historical Drama", "synopsis": "A family's story during the tumultuous martial law period in the 1970s.", "release_date": date(2002, 1, 1)},
            {"title": "Maynila sa mga Kuko ng Liwanag", "genre": "Drama", "synopsis": "A man searches for his lost love in the harsh urban landscape of Manila.", "release_date": date(1975, 5, 16)},
            {"title": "Magnifico", "genre": "Family Drama", "synopsis": "A boy tries to help his family and his ailing grandmother in a small town.", "release_date": date(2003, 1, 29)},
            {"title": "Bayaning Third World", "genre": "Historical", "synopsis": "A fictional investigation into the life and myths of José Rizal.", "release_date": date(2000, 3, 8)},
            {"title": "Ang Babae sa Septic Tank", "genre": "Comedy", "synopsis": "Filmmakers attempt to create a movie about poverty in the Philippines.", "release_date": date(2011, 7, 6)},
            {"title": "Tadhana", "genre": "Romance", "synopsis": "A woman finds solace after a breakup during a road trip.", "release_date": date(2014, 11, 9)},
            {"title": "Goyo: Ang Batang Heneral", "genre": "Historical Drama", "synopsis": "The story of Gregorio 'Goyo' del Pilar, one of the youngest generals in the Philippine Revolution.", "release_date": date(2018, 9, 5)},
            {"title": "Heneral Luna", "genre": "Historical Drama", "synopsis": "The life and struggles of General Antonio Luna during the Philippine-American War.", "release_date": date(2015, 9, 9)},
            {"title": "Kita Kita", "genre": "Romantic Comedy", "synopsis": "A blind woman finds unexpected love with her persistent suitor.", "release_date": date(2017, 7, 19)},
            {"title": "One More Chance", "genre": "Romance", "synopsis": "A couple tries to find their way back to each other after a painful breakup.", "release_date": date(2007, 11, 14)},
            {"title": "On the Job", "genre": "Action Thriller", "synopsis": "Prisoners-turned-hitmen work for corrupt politicians.", "release_date": date(2013, 5, 24)},
            {"title": "BuyBust", "genre": "Action", "synopsis": "An anti-narcotics squad gets trapped in a deadly slum during a drug bust.", "release_date": date(2018, 8, 1)},
            {"title": "Sana Dati", "genre": "Romance Drama", "synopsis": "A bride confronts her past when an unexpected guest arrives at her wedding.", "release_date": date(2013, 7, 27)},
            {"title": "That Thing Called Tadhana", "genre": "Romantic Comedy", "synopsis": "Two strangers bond over heartbreak during a spontaneous trip to Baguio.", "release_date": date(2014, 11, 9)},
            {"title": "Patay na si Hesus", "genre": "Dark Comedy", "synopsis": "A mother and her children embark on a road trip to attend a funeral.", "release_date": date(2016, 8, 14)},
            {"title": "Respeto", "genre": "Drama", "synopsis": "A young rapper finds solace and mentorship amidst social struggles.", "release_date": date(2017, 8, 2)},
            {"title": "Die Beautiful", "genre": "Drama/Comedy", "synopsis": "A transgender woman’s life is celebrated through her final wishes.", "release_date": date(2016, 12, 25)},
        ]

        for film_data in films_data:
            Film.objects.create(**film_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample Pinoy films!'))
