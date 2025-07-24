from core.settings import Config, Platform


def test_config_loading():
    """Test loading configuration from YAML"""
    config = Config.load_from_yaml()

    # Check that configuration is loaded correctly
    assert config.browser.headless is False
    assert config.browser.device.type == "iPhone 12"
    assert config.test.base_url == "http://localhost:3000"
    assert config.environment.platform == Platform.WEB


def test_platform_enum():
    """Test platform enum values"""
    assert Platform.WEB.value == "WEB"
    assert Platform.MOBILE.value == "MOBILE"


def test_context_creation():
    """Test context creation"""
    from core.context import PlaywrightContextFactory
    from core.settings import Config

    config = Config.load_from_yaml()
    factory = PlaywrightContextFactory(config)

    # Create browser
    browser = factory.create_browser()

    # Check that browser is created
    assert browser is not None

    # Create page
    page = factory.create_page(browser)

    # Check that page is created
    assert page is not None

    # Close browser
    browser.playwright.close()
