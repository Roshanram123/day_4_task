
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# Grade calculation
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Initialize session state
if "students" not in st.session_state:
    st.session_state.students = []


# Page heading
st.title("🎓 Student Grade Manager")
st.write("Manage student marks and track class performance.")

st.divider()


# Add Student Form
st.subheader("➕ Add New Student")

with st.form("add_student", clear_on_submit=True):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Student Name",
            placeholder="Enter student name"
        )

    with col2:
        mark = st.number_input(
            "Student Mark",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    submitted = st.form_submit_button(
        "Add Student",
        use_container_width=True
    )

    if submitted:

        if not name.strip():
            st.error("Please enter student name.")

        else:
            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


st.divider()


# Student Table
st.subheader("📋 Student Records")

if st.session_state.students:

    st.dataframe(
        st.session_state.students,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # Calculate class statistics
    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Display metrics
    st.subheader("📊 Class Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Class Average",
            value=f"{average:.2f}"
        )

    with col2:
        st.metric(
            label="Highest Mark",
            value=highest
        )

    with col3:
        st.metric(
            label="Lowest Mark",
            value=lowest
        )

    st.divider()

    # Delete student
    st.subheader("🗑️ Remove Student")

    selected_student = st.selectbox(
        "Select student",
        options=range(len(st.session_state.students)),
        format_func=lambda i: st.session_state.students[i]["Name"]
    )

    if st.button("Delete Selected Student"):
        removed = st.session_state.students.pop(selected_student)
        st.success(f"{removed['Name']} removed successfully!")
        st.rerun()

else:
    st.info("No students added yet. Add your first student above!")

