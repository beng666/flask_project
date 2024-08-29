from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def get_db_connection():
    conn = sqlite3.connect('quiz0.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    # Sayfa her baştan açıldığında best_score sıfırlanır, ancak actual_best_score saklanır
    session['best_score'] = 0

    if 'actual_best_score' not in session:
        session['actual_best_score'] = 0

    conn = get_db_connection()
    # Veritabanından rastgele 4 soru seçiyoruz ve session'da saklıyoruz
    questions = conn.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 4').fetchall()
    session['questions'] = [dict(q) for q in questions]  # Soruları session'da saklıyoruz
    conn.close()
    return render_template('quiz.html', questions=session['questions'], best_score=session['actual_best_score'])


@app.route('/submit', methods=['POST'])
def submit():
    questions = session.get('questions', [])

    # Eğer soru yoksa, kullanıcıyı uyaralım
    if not questions:
        return "Sınav sırasında bir hata oluştu. Lütfen tekrar deneyin."

    score = 0

    for i, question in enumerate(questions):
        selected_answer = request.form.get(f'question_{i}')
        if selected_answer and selected_answer.strip().lower() == question['answer'].strip().lower():
            score += 1

    percentage_score = (score / len(questions)) * 100 if len(questions) > 0 else 0
    username = request.form.get('username')

    conn = get_db_connection()
    conn.execute('INSERT INTO results (username, score) VALUES (?, ?)', (username, percentage_score))
    conn.commit()
    conn.close()

    # En yüksek skoru güncelle
    session['actual_best_score'] = max(session.get('actual_best_score', 0), percentage_score)

    return redirect(url_for('result', score=percentage_score))


@app.route('/result')
def result():
    score = request.args.get('score', 0)
    return render_template('result.html', score=score, best_score=session.get('actual_best_score', 0))


@app.route('/reset')
def reset():
    # Yeni sınav başlatıldığında session sıfırlanır
    session.pop('quiz_started', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
