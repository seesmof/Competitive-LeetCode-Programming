Виконати завдання лабораторної роботи #6 з використанням бібліотеки jQuery. Приділити найбільшу увагу роботі з селекторами та подіями.

```
<script>
  $(document).ready(function() {
    let errorModal = $("#error-modal");
    let errorParagraph = $("#error-paragraph");
    let errorButton = $("#error-dismiss");

    let nameInput = $("#name");
    let emailInput = $("#email");
    let phoneInput = $("#phone");
    let messageInput = $("#message");
    let formSubmitButton = $("#form-submit");

    let messageCharactersNumber = $("#number-of-characters");

    messageInput.on("input", function() {
      let value = $(this).val();
      messageCharactersNumber.text(value.length);
    });

    function toggleErrorMessage() {
      errorModal.toggleClass("hidden");
    }

    function clearInputs() {
      nameInput.val("");
      emailInput.val("");
      phoneInput.val("");
      messageInput.val("");
    }

    function addRedBorder(input) {
      input.removeClass("border-none").addClass("border-red-500 border-2");
    }

    function removeRedBorder(input) {
      input.removeClass("border-red-500 border-2").addClass("border-none");
    }

    function addRedBackground(input) {
      input.removeClass("bg-slate-100").addClass("bg-red-200");
    }

    function removeRedBackground(input) {
      input.removeClass("bg-red-200").addClass("bg-slate-100");
    }

    function validateName(input) {
      const regex = /^[a-zA-Zа-яА-ЯіІїЇєЄґҐ\s]+$/;

      if (!regex.test(input.val())) {
        const paragraph = "Ім'я має містити лише Українські або Англійські літери.";

        return {
          valid: false,
          message: paragraph,
        };
      } else {
        return {
          valid: true,
          message: "",
        };
      }
    }

    function validateEmail(input) {
      const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

      if (!regex.test(input.val())) {
        const paragraph = "Електронна пошта має бути у форматі example@company.com.";

        return {
          valid: false,
          message: paragraph,
        };
      } else {
        return {
          valid: true,
          message: "",
        };
      }
    }

    function validatePhone(input) {
      const regex = /^[\s\d()+-]+$/;

      if (!regex.test(input.val())) {
        const paragraph = "Телефон має містити лише цифри, пробіли або знаки +, -, ().";

        return {
          valid: false,
          message: paragraph,
        };
      } else {
        return {
          valid: true,
          message: "",
        };
      }
    }

    formSubmitButton.on("click", function(event) {
      event.preventDefault();

      const nameResults = validateName(nameInput);
      const nameValid = nameResults.valid;
      const nameMessage = nameResults.message;

      const emailResults = validateEmail(emailInput);
      const emailValid = emailResults.valid;
      const emailMessage = emailResults.message;

      const phoneResults = validatePhone(phoneInput);
      const phoneValid = phoneResults.valid;
      const phoneMessage = phoneResults.message;

      let inputsEmpty = false;
      const errorParagraphMessage = `${nameMessage} ${emailMessage} ${phoneMessage}`;

      if (nameInput.val() === "") {
        addRedBorder(nameInput);
        inputsEmpty = true;
      } else if (!nameValid) {
        addRedBorder(nameInput);
        addRedBackground(nameInput);
      }

      if (emailInput.val() === "") {
        addRedBorder(emailInput);
        inputsEmpty = true;
      } else if (!emailValid) {
        addRedBorder(emailInput);
        addRedBackground(emailInput);
      }

      if (phoneInput.val() === "") {
        addRedBorder(phoneInput);
        inputsEmpty = true;
      } else if (!phoneValid) {
        addRedBorder(phoneInput);
        addRedBackground(phoneInput);
      }

      if (!nameValid || !emailValid || !phoneValid) {
        errorParagraph.text(errorParagraphMessage);
        toggleErrorMessage();
      } else if (!inputsEmpty) {
        clearInputs();
      }
    });

    errorButton.on("click", function() {
      toggleErrorMessage();
      removeRedBorder(nameInput);
      removeRedBackground(nameInput);
      removeRedBorder(emailInput);
      removeRedBackground(emailInput);
      removeRedBorder(phoneInput);
      removeRedBackground(phoneInput);
      clearInputs();
    });

    errorModal
```
