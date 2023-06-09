from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..services.gpt_service import get_gpt_response
from ..models.user import User
from ..models.message import Message, add_message
from flask_app.database import db


gpt_routes = Blueprint('gpt_routes', __name__)

@gpt_routes.route('/chat', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        message = data.get('message', 'No message found in JSON object')
        gpt_res = get_gpt_response(message)
        response = {
            'status': 'success',
            'received_message_from_gpt': gpt_res
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'status': 'error', message:str(e)}), 500

@gpt_routes.route('/messages', methods=['GET'])
@login_required
def messages():
    return render_template("messages.html", user=current_user)

@gpt_routes.route('/gpt/form', methods=['GET'])
@login_required
def render_gpt_form():
    return render_template("gpt-form.html", user=current_user)

@gpt_routes.route('/submit_message', methods=['POST'])
@login_required
def submit_message():
    user_id = current_user.id
    content = request.form['msg']
    print(content)
     # Get message history from the database
    message_history = Message.query.filter_by(user_id=user_id).order_by(Message.ts.asc()).all()
    print(message_history,'submit')
    try:
        answer = get_gpt_response(content, message_history)
    except Exception as e:
        flash('Error on gpt response, Please try agian', category='danger')
        return jsonify({'status': 'error', 'message':str(e)}), 500
    user = User.query.get(user_id)

    if user:
        add_message(user, "user", content)  # Save the user message
        add_message(user, "assistant", answer)  # Save the assistant message
        return redirect(url_for('gpt_routes.messages'))

    return jsonify({'status': 'error', 'message': 'User not found'}), 404



# route for getting all the messages array as json
@gpt_routes.route('/api/msg' , methods=['GET'])
def get_messages():
    msgs = Message.query.all()
    msgs_data = [{'id': msg.id, 'role': msg.role, 'content': msg.content, 'ts': msg.ts} for msg in msgs]
    print(msgs_data)
    return jsonify(msgs_data)