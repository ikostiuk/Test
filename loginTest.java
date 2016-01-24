/**
 * Created by Ivan.Kostiuk on 23.01.2016.
 */

import org.junit.Test;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class loginTest{
    @Test
    public void login(){
        WebDriver driver = new FirefoxDriver();
        WebDriverWait wait = new WebDriverWait(driver, 5);

        // Opening main application page:
        driver.get("http://streamtv.net.ua/base");

        String loginFormHeader = driver.findElement(By.xpath("/html/body/div/div/div/div/div/div[1]")).getText();
        Assert.assertTrue("Login form name verification failed", loginFormHeader.contains("Login"));

        // Logging into the application by inserting credentials:
        WebElement loginField = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//input[@placeholder='Login']")));
        loginField.sendKeys("auto");

        WebElement passwordField = driver.findElement(By.xpath("//input[@placeholder='Password']"));
        passwordField.sendKeys("test");

        // Pressing 'Login' button:
        WebElement loginButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div/div/div/div/div/div[2]/form/button")));
        Assert.assertTrue("Failed to log in. \'Login\' button is disabled", loginButton.isEnabled());
        loginButton.click();

        // Verify opening wrestlers tab on pressing Login button:
        String wrestlersTabText = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("/html/body/div/div/div/div/div/ul/li/a"))).getText();
        Assert.assertTrue("No Wrestlers tab seen on pressing Login button", wrestlersTabText.contains("Wrestlers"));
        driver.close();
    }
}
