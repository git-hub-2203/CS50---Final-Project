function togglePasswordVisibility(element) {
  const input = typeof element === 'string' ? document.getElementById(element) : element;
  const button = input.parentElement.querySelector('button');
  const icon = button.querySelector('i');

  if (input.type === 'password') {
    input.type = 'text';
    icon.classList.remove('fa-eye');
    icon.classList.add('fa-eye-slash');
  } else {
    input.type = 'password';
    icon.classList.remove('fa-eye-slash');
    icon.classList.add('fa-eye');
  }
}
