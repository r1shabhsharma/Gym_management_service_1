# membership_service 
from flask import Flask, request, jsonify
from models import db, Membership

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Root route
@app.route('/')
def home():
    return "Welcome to the Gym Management System API!"

# Route to add a new membership
@app.route('/memberships', methods=['POST'])
def add_membership():
    data = request.get_json()
    new_membership = Membership(
        member_id=data['member_id'],
        start_date=data['start_date'],
        expiry_date=data['expiry_date']
    )
    db.session.add(new_membership)
    db.session.commit()
    return jsonify({'message': 'Membership added successfully'}), 201

# Route to get all memberships
@app.route('/memberships', methods=['GET'])
def get_memberships():
    memberships = Membership.query.all()
    return jsonify([membership.to_dict() for membership in memberships])

# Route to update a membership
@app.route('/memberships/<int:id>', methods=['PUT'])
def update_membership(id):
    data = request.get_json()
    membership = Membership.query.get(id)
    if membership:
        membership.start_date = data.get('start_date', membership.start_date)
        membership.expiry_date = data.get('expiry_date', membership.expiry_date)
        db.session.commit()
        return jsonify({'message': 'Membership updated successfully'})
    return jsonify({'message': 'Membership not found'}), 404

# Route to delete a membership
@app.route('/memberships/<int:id>', methods=['DELETE'])
def delete_membership(id):
    membership = Membership.query.get(id)
    if membership:
        db.session.delete(membership)
        db.session.commit()
        return jsonify({'message': 'Membership deleted successfully'})
    return jsonify({'message': 'Membership not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)