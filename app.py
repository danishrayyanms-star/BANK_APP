import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SBI Bank App", page_icon="🏦", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
background: linear-gradient(to right,#e3f2fd,#ffffff);
}

.stButton>button {
background-color: #0d6efd;
color: white;
font-weight: bold;
border-radius: 10px;
padding: 10px;
width: 100%;
}

.stButton>button:hover {
background-color: #084298;
color:white;
}

.bank-card {
background-color:white;
padding:25px;
border-radius:15px;
box-shadow:0px 0px 15px rgba(0,0,0,0.1);
}

.header {
text-align:center;
padding:10px;
color:#0d6efd;
font-size:35px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------- BANK CLASS ----------
class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"Transaction Successful. Collected ₹{amount}"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Successful. Total Balance: ₹{self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"Mobile number updated: {self.mobile_number}"

    def check_balance(self):
        return f"Total Account Balance: ₹{self.balance}"


# ---------- HEADER ----------
st.markdown('<div class="header">🏦 SBI Digital Banking</div>', unsafe_allow_html=True)
st.write("Welcome to your secure online banking system.")

# ---------- SESSION ----------
if "account" not in st.session_state:
    st.session_state.account = None


# ---------- SIDEBAR ----------
st.sidebar.title("📋 Banking Menu")

menu = ["Create Account", "Deposit", "Withdraw", "Update Mobile", "Check Balance"]

choice = st.sidebar.radio("Select Option", menu)


# ---------- CREATE ACCOUNT ----------
if choice == "Create Account":

    st.markdown('<div class="bank-card">', unsafe_allow_html=True)

    st.subheader("📝 Create New Account")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=18)

    with col2:
        account_number = st.text_input("Account Number")
        mobile = st.text_input("Mobile Number")

    balance = st.number_input("Initial Deposit", min_value=0)

    if st.button("Create Account"):
        st.session_state.account = BankApplication(name, account_number, age, mobile, balance)
        st.success("✅ Account Created Successfully!")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- DEPOSIT ----------
elif choice == "Deposit":

    st.markdown('<div class="bank-card">', unsafe_allow_html=True)

    st.subheader("💰 Deposit Money")

    if st.session_state.account:

        amount = st.number_input("Enter Amount")

        if st.button("Deposit Money"):
            result = st.session_state.account.deposit(amount)
            st.success(result)

    else:
        st.warning("⚠ Please create an account first.")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- WITHDRAW ----------
elif choice == "Withdraw":

    st.markdown('<div class="bank-card">', unsafe_allow_html=True)

    st.subheader("💳 Withdraw Money")

    if st.session_state.account:

        amount = st.number_input("Enter Amount")

        if st.button("Withdraw Money"):
            result = st.session_state.account.withdraw(amount)
            st.success(result)

    else:
        st.warning("⚠ Please create an account first.")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- UPDATE MOBILE ----------
elif choice == "Update Mobile":

    st.markdown('<div class="bank-card">', unsafe_allow_html=True)

    st.subheader("📱 Update Mobile Number")

    if st.session_state.account:

        new_mobile = st.text_input("Enter New Mobile Number")

        if st.button("Update Mobile"):
            result = st.session_state.account.update_mobile(new_mobile)
            st.success(result)

    else:
        st.warning("⚠ Please create an account first.")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- CHECK BALANCE ----------
elif choice == "Check Balance":

    st.markdown('<div class="bank-card">', unsafe_allow_html=True)

    st.subheader("🏦 Account Balance")

    if st.session_state.account:
        balance = st.session_state.account.check_balance()
        st.success(balance)
    else:
        st.warning("⚠ Please create an account first.")

    st.markdown('</div>', unsafe_allow_html=True)