const form = document.querySelector("form"),
      nextBtn = form.querySelector(".nextBtn"),
      backBtn = form.querySelector(".backBtn"),
      allInput = form.querySelectorAll(".first input, .first select"),
      firstForm = form.querySelector(".form.first"),
      secondForm = form.querySelector(".form.second");

nextBtn.addEventListener("click", () => {
    let allValid = true;

    allInput.forEach(input => {
        if (input.value === "") {
            allValid = false;
            input.classList.add("invalid");
        } else {
            input.classList.remove("invalid");
        }
    });

    if (allValid) {
        firstForm.classList.remove('active');
        secondForm.classList.add('active');
    }
});

backBtn.addEventListener("click", () => {
    secondForm.classList.remove('active');
    firstForm.classList.add('active');
});
