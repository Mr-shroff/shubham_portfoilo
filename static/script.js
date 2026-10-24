const menuToggle = document.querySelector("#menuToggle");
const mainNav = document.querySelector("#mainNav");

if (menuToggle && mainNav) {
  menuToggle.addEventListener("click", () => {
    const isOpen = mainNav.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
  });

  mainNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      mainNav.classList.remove("open");
      menuToggle.setAttribute("aria-expanded", "false");
    });
  });
}

const contactForm = document.querySelector("#contactForm");
const feedback = document.querySelector("#formFeedback");

if (contactForm && feedback) {
  contactForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    feedback.textContent = "Checking your message...";
    feedback.classList.remove("error");

    const formData = new FormData(contactForm);
    const payload = Object.fromEntries(formData.entries());

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const result = await response.json();

      if (!response.ok || !result.ok) {
        throw new Error(result.error || "Something went wrong.");
      }

      feedback.textContent = result.message;
      contactForm.reset();
    } catch (error) {
      feedback.textContent = error.message || "Couldn't reach the server. Is Flask running?";
      feedback.classList.add("error");
    }
  });
}
