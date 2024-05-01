from kerykeion.charts.kerykeion_chart_svg import KerykeionChartSVG
from kerykeion.astrological_subject import AstrologicalSubject
from pathlib import Path
from flask import Flask, request, send_file

app = Flask(__name__)
@app.route('/createSVG', methods=['POST'])

def generar_archivo():
    data = request.json

    name = data.get('name')
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')
    hour = data.get('hour')
    minute = data.get('minute')
    city = data.get('city', 'London')
    nation = data.get('nation', 'GB')
    style = data.get('style')
    font = data.get('font', "Belgan Aesthetic")
    bg_image_wheel = data.get('bg_image_wheel', None)
    bg_image = data.get('bg_image', None)
    bg_color = data.get('bg_color', None)

    if style.lower() == "bright":
        style_path = Path("kerykeion/charts/bright.json")
    else:
        style_path = Path("kerykeion/charts/dark.json")

    # create instances
    subject = AstrologicalSubject(name, year, month, day, hour, minute, city, nation)
    chart = KerykeionChartSVG(subject, "Natal", None, "output", style_path, font, bg_color, bg_image, bg_image_wheel)
    chart.makeSVG()
    svg_file_path = chart.chartname
    return send_file(svg_file_path,
                     mimetype='image/svg+xml',
                     as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)


# TODO: Limpiar proyecto¿?
# TODO: Subir el proyecto a koyeb.app (Quizá con la cuenta de chambeadevs)
# TODO: Si usamos la cuenta de chambeadevs hay que hacerle un github
# TODO:subir la colección de postman a rapidapi