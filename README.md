
# Brain Rot Checker

The "Brain Rot Checker" application is a web-based expert system that helps users detect indications of brain rot through a series of questions and provides recommendations based on the analysis results. This application is built using **Flask**, **MongoDB**, and **Bootstrap 5** for the user interface.

## Features

- **User Registration and Login**: Users can create an account and log in to access the application.
- **User Dashboard**: Users can view their diagnosis history.
- **Brain Rot Diagnosis**: Users can fill out a form to assess their condition based on predefined criteria.
- **Diagnosis History**: Users can view their diagnosis history in daily, monthly, yearly, or custom formats.
- **Admin Panel**: Admin can modify the weighting and recommendations for the diagnosis.

## Technologies

- **Flask**: Python web framework for the server-side application.
- **MongoDB Atlas**: NoSQL database to store user data and diagnosis history.
- **Bootstrap 5**: CSS framework for responsive design.

## Project Structure

```
brain_rot_checker/
├── app.py          # Main Flask file
├── templates/      # Folder for HTML files
│   ├── base.html   # Base template (reusable)
│   ├── index.html  # Input form page, extends base.html
│   ├── result.html # Diagnosis result page, extends base.html
├── static/         # Folder for additional CSS/JS files (if any)
│   ├── style.css   # (optional)
```

## Installation

### Prerequisites

Make sure you have Python 3.x installed and have access to MongoDB Atlas. Then, install the required dependencies:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/brain-rot-checker.git
   cd brain-rot-checker
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/MacOS
   venv\Scripts ctivate      # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB Atlas**:
   - Sign up at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
   - Create a new database and get the connection URI to use in the app.

5. **Create a `.env` file** to store MongoDB configuration:
   ```
   MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/brain_rot_checker?retryWrites=true&w=majority
   ```

### Running the Application

Once everything is set up, you can run the application using the following command:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Registration / Login**: New users can register, while existing users can log in with their email and password.
2. **Fill out the Diagnosis Form**: After logging in, users can fill out the form to evaluate brain rot symptoms.
3. **View Results**: After submitting the form, the diagnosis results will be displayed along with recommendations.
4. **View Diagnosis History**: Users can access their diagnosis history on the dashboard.

## Contributing

If you would like to contribute to this project, feel free to **fork** the repository and create a pull request with your changes.

1. **Fork this repository**.
2. **Clone your forked repository**:
   ```bash
   git clone https://github.com/username/brain-rot-checker.git
   ```
3. **Create a new branch**:
   ```bash
   git checkout -b branch-name
   ```
4. **Commit your changes**:
   ```bash
   git commit -am 'Add new feature'
   ```
5. **Push to your branch**:
   ```bash
   git push origin branch-name
   ```
6. **Create a pull request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for using **Brain Rot Checker**! We hope this application can help in detecting brain rot indications more efficiently.
