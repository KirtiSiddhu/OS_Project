from flask import Flask, render_template, request, jsonify
from directory.manager import DirectoryManager
from ai.model import AIModel

app = Flask(__name__)

# Initialize AI model and DirectoryManager
ai_model = AIModel()
directory_manager = DirectoryManager(ai_model)

@app.route("/")
def index():
    """Serve the HTML frontend."""
    return render_template("index.html")

@app.route("/api/command", methods=["POST"])
def handle_command():
    """Handle commands sent from the frontend."""
    data = request.json
    command = data.get("command", "").lower()

    if "add entry" in command:
        path = data.get("path", "")
        directory_manager.add_entry(path)
        return jsonify({"message": f"Entry '{path}' added successfully."})
    elif "remove entry" in command:
        path = data.get("path", "")
        directory_manager.remove_entry(path)
        return jsonify({"message": f"Entry '{path}' removed successfully."})
    elif "list entries" in command:
        entries = directory_manager.list_entries()
        return jsonify({"entries": entries})
    elif "create file" in command:
        path = data.get("path", "")
        file_name = data.get("file_name", "")
        content = data.get("content", "")
        directory_manager.create_file(path, file_name, content)
        return jsonify({"message": f"File '{file_name}' created successfully in '{path}'."})
    elif "remove file" in command:
        file_path = data.get("file_path", "")
        directory_manager.remove_file(file_path)
        return jsonify({"message": f"File '{file_path}' removed successfully."})
    else:
        return jsonify({"error": "Invalid command."}), 400

if __name__ == "__main__":
    app.run(debug=True)