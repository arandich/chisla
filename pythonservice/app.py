from flask import Flask, request, jsonify
import random
from flask_cors import CORS  # Импорт модуля CORS

from number import rec_digit # Замените на ваш модуль распознавания

app = Flask(__name__)
CORS(app)  # Применение CORS к приложению

@app.route('/api/recognize', methods=['POST'])
def recognize():
    if 'image' in request.files:
        image = request.files['image']

        # Сохранение изображения
        name = 'number' + str(random.randint(10, 99)) + '.png'
        image.save(name)
        result = rec_digit(name)
        return jsonify({'result': result})
    else:
        return 'Изображение не найдено в запросе.'



if __name__ == '__main__':
    app.run(debug=True)
