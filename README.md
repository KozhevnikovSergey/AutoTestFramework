# AutoTestFramework

A portfolio‑style test automation framework designed to cleanly separate **test code** from **tooling code** (Appium, Selenium, Playwright, etc.), ensuring maximum flexibility and reusability.

## Core Principles

- **Separation of Concerns**  
  - All test scenarios and step definitions live in `tests/` (BDD‑style or classic pytest).  
  - All driver‑specific adapters and wrappers live in `drivers/` (Selenium, Playwright, Appium, etc.).  
- **Modular Portfolio Structure**  
  - Each component is organized into its own module to showcase clean architecture and best practices.  
- **Configurable**  
  - Switch between web and mobile platforms, different browsers, headless modes, timeouts, etc., via `config.yaml` or environment variables—no changes to test code required.

## ⚙️ Work in Progress

This project is actively being developed and is not a final version.  
Planned additions include:
- Centralized logging  
- Appium support  
- Mocking  
- Dockerfile & containerized test environment  
- CI/CD integration (tests with mocks on every PR) 
