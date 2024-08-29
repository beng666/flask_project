import sqlite3

def create_database():
    connection = sqlite3.connect('quiz0.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                        id INTEGER PRIMARY KEY,
                        question TEXT NOT NULL,
                        option1 TEXT NOT NULL,
                        option2 TEXT NOT NULL,
                        option3 TEXT NOT NULL,
                        answer TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        score INTEGER NOT NULL
                    )''')

    # NLP konusuyla ilgili 20 soru ekleyelim
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("NLP nedir?", 'Yapay zeka', 'Doğal dil işleme', 'Makine öğrenmesi', 'Doğal dil işleme')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Doğal dil işleme hangi alanlarda kullanılır?", 'Ses tanıma', 'Görüntü işleme', 'Veri tabanı yönetimi', 'Ses tanıma')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Bir cümlenin dilbilgisel yapısını çözümleme süreci nedir?", 'Anlambilim', 'Morfoloji', 'Sözdizim', 'Sözdizim')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Kelime köklerini bulma işlemi nedir?", 'Stemming', 'Lemmatization', 'Tokenization', 'Stemming')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("NLP'de kelimelerin anlamlarını modellemek için kullanılan yaygın bir yöntem nedir?", 'One-hot encoding', 'Word embeddings', 'Bag of Words', 'Word embeddings')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Hangi teknik, metin verilerini sabit boyutlu bir vektöre dönüştürür?", 'TF-IDF', 'Bag of Words', 'Word embeddings', 'TF-IDF')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Hangi NLP görevinde metinler, belirli bir etikete veya sınıfa atanır?", 'Dil modelleme', 'Makine çevirisi', 'Metin sınıflandırma', 'Metin sınıflandırma')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Metin verilerinden bilgi çıkarma işlemi nedir?", 'Bilgi çıkarma', 'Metin özetleme', 'Duygu analizi', 'Bilgi çıkarma')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Bir metindeki anlamsal ilişkilerin çıkarılması işlemi nedir?", 'Anlambilim', 'Sözdizim', 'Morfoloji', 'Anlambilim')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("NLP'de 'sentiment analysis' ne anlama gelir?", 'Cümlelerin dilbilgisel doğruluğunu analiz etme', 'Bir metnin duygu durumunu analiz etme', 'Metnin bağlamını belirleme', 'Bir metnin duygu durumunu analiz etme')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Hangi teknik, bir cümlenin anlamını daha büyük bir yapıya entegre eder?", 'Makine öğrenmesi', 'Anlambilimsel ağlar', 'Parçacık dil modeli', 'Anlambilimsel ağlar')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Hangi teknik, bir kelimenin bağlamını dikkate alarak anlamını bulur?", 'Lemmatization', 'Word2Vec', 'N-gram', 'Word2Vec')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Hangi model, büyük metin verilerinden dil kurallarını öğrenir?", 'Destek vektör makineleri', 'LSTM', 'Transformers', 'Transformers')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Duygu analizi, metinlerin hangi yönünü analiz eder?", 'Dilbilgisel yapı', 'Duygu durumu', 'Anlamsal içerik', 'Duygu durumu')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("NLP'de kullanılan popüler bir önişleme adımı nedir?", 'Stop words kaldırma', 'Veri temizleme', 'Veri dönüştürme', 'Stop words kaldırma')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Makine çevirisi hangi NLP uygulamasına örnektir?", 'Metin sınıflandırma', 'Dil modelleme', 'Makine çevirisi', 'Makine çevirisi')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Hangi NLP görevi, metnin otomatik olarak özetlenmesini sağlar?", 'Özetleme', 'Metin sınıflandırma', 'Duygu analizi', 'Özetleme')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Bir cümledeki kelimeleri anlamlarına göre gruplama işlemi nedir?", 'Sözdizim', 'Anlambilim', 'Morfoloji', 'Anlambilim')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Kelime köklerini bulma işlemi, NLP'de hangi adım olarak adlandırılır?", 'Stemming', 'Tokenization', 'Lemmatization', 'Stemming')''')
    cursor.execute('''INSERT INTO questions (question, option1, option2, option3, answer)
                      VALUES ("Doğal Dil İşleme'de kullanılan dil modeli nedir?", 'Bag of Words', 'GPT', 'LSTM', 'GPT')''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_database()
