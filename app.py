from flask import Flask, request, send_file, render_template
import base64
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    image_data = data['canvasData']
    image_data = image_data.split(';base64,')[1]
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))

    img_io = io.BytesIO()
    image.save(img_io, 'PNG', quality=100)
    img_io.seek(0)

    return send_file(
        img_io,
        mimetype='image/png',
        as_attachment=True,
        download_name='downloaded_image.png'
    )
def create_image(data):
    # Placeholder for image creation logic
    image = Image.new('RGB', (1000, 1000), 'white')
    return image

#Uncomment for local deployment
#if __name__ == '__main__':
#   app.run(debug=True, port=5001)