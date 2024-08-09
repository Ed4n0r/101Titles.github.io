from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

# Каталог для хранения загруженных файлов
UPLOAD_FOLDER = 'uploads'

# Создание каталога, если он не существует
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Маршрут для загрузки файла
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Получаем загруженный файл
        file = request.files['file']

        # Сохраняем файл в каталоге
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        return jsonify({'success': True})

# Маршрут для поиска файлов
@app.route('/search', methods=['GET'])
def search_files():
    search_term = request.args.get('search', '')

    # Получаем список файлов из каталога
    files = os.listdir(UPLOAD_FOLDER)
     # Фильтруем файлы по названию
     filtered_files = [file for file in files if search_term in file]

    return jsonify({'files': filtered_files})


# Маршрут для скачивания файла
@app.route('/download', methods=['GET'])
def download_file():
    file_name = request.args.get('file', '')

    # Проверяем, существует ли файл
    if os.path.exists(os.path.join(UPLOAD_FOLDER, file_name)):
        return send_file(os.path.join(UPLOAD_FOLDER, file_name), as_attachment=True)
    else:
        return jsonify({'success': False, 'error': 'File not found'})


# Маршрут для удаления файла
@app.route('/delete', methods=['DELETE'])
def delete_file():
    file_name = request.args.get('file', '')

    # Проверяем, существует ли файл
    if os.path.exists(os.path.join(UPLOAD_FOLDER, file_name)):
        os.remove(os.path.join(UPLOAD_FOLDER, file_name))
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'File not found'})


if __name__ == '__main__':
    app.run(debug=True)