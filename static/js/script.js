function copyPassword(password) {
    navigator.clipboard.writeText(password).then(() => {
        const notification = document.getElementById('notification');
        notification.classList.remove('hidden');
        notification.classList.add('show');
        setTimeout(() => {
            notification.classList.remove('show');
            notification.classList.add('hidden');
        }, 2000); // محو شدن بعد از 3 ثانیه
    }).catch(() => {
        alert('خطا در کپی کردن رمز!');
    });
}

function showForm() {
  const formSection = document.getElementById("formSection");
  formSection.classList.remove("hidden");
  formSection.classList.add("visible");
}

function hideForm() {
  const formSection = document.getElementById("formSection");
  formSection.classList.remove("visible");
  formSection.classList.add("hidden");
}