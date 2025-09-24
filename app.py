from flask import Flask, jsonify
from owlready2 import get_ontology

app = Flask(__name__)

# Load ontology at startup
#ONTO_PATH = "/path/to/your/ontology.owl"
ONTO_PATH = "https://www.ai4c2ps.eu/ontologies/2024/1.0.0/AI4C2PS.owl"
ontology = get_ontology(ONTO_PATH).load()

@app.route('/classes', methods=['GET'])
def get_classes():
    # Get all classes from the ontology
    class_iris = [cls.iri for cls in ontology.classes()]
    return jsonify(class_iris), 200

if __name__ == '__main__':
    app.run(debug=True)
