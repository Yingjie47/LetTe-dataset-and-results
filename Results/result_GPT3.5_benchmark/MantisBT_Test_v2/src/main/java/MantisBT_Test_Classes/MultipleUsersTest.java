package MantisBT_Test_Classes;

//import config.DriverConfig;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.AssertJUnit;
import org.testng.annotations.*;
import MantisBT_Test_Classes.sql.Constants;
//import testcases.mantisbt.model_based_dataset.po.User;

import java.util.concurrent.TimeUnit;

public class MultipleUsersTest {
	private static WebDriver driver;

	@BeforeMethod

	public void setUp() throws Exception {
		System.setProperty("webdriver.chrome.driver",
				"D:\\anaconda3\\chromedriver.exe");
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		driver.get(Constants.BASE_URL);
		// Login User Administrator
		driver.findElement(By.name("username")).clear();
		driver.findElement(By.name("username")).sendKeys(Constants.Mantisbt_ADMIN_USER_NAME);
		driver.findElement(By.name("password")).clear();
		driver.findElement(By.name("password")).sendKeys(Constants.Mantisbt_ADMIN_PASSWORD);
		driver.findElement(By.xpath("//input[@value='Login']")).click();
		Thread.sleep(2000);
		// TODO: User.deleteUser("Demo User1");
		// TODO: User.deleteUser("Demo User2");
	}

	@Test(priority = 0)
	public static void MultipleUsersTest() throws Exception {
		driver.findElement(By.xpath("//a[contains(text(),'Manage')]")).click();

		driver.findElement(By.xpath("//a[contains(text(),'Manage Users')]")).click();
		driver.findElement(By.xpath("//input[@value='Create New Account']")).click();
		Thread.sleep(1000);
		// Submit Form
		Thread.sleep(1000);
		driver.findElement(By.name("username")).clear();
		driver.findElement(By.name("username")).sendKeys("Demo User1");
		driver.findElement(By.name("realname")).clear();
		driver.findElement(By.name("realname")).sendKeys("Demo User1");
		driver.findElement(By.name("email")).sendKeys("demo@gmail.com");
		driver.findElement(By.xpath("//input[@value='Create User']")).click();
		driver.findElement(By.xpath("//a[contains(text(),'Manage')]")).click();
		Thread.sleep(3000);
		AssertJUnit.assertEquals(driver.findElement(By.xpath("//a[text()='Demo User1']")).getText(),
				"Demo User1");
		driver.findElement(By.xpath("//a[contains(text(),'Manage')]")).click();

		driver.findElement(By.xpath("//a[contains(text(),'Manage Users')]")).click();
		driver.findElement(By.xpath("//input[@value='Create New Account']")).click();
		Thread.sleep(1000);
		// Submit Form
		Thread.sleep(1000);
		driver.findElement(By.name("username")).clear();
		driver.findElement(By.name("username")).sendKeys("Demo User2");
		driver.findElement(By.name("realname")).clear();
		driver.findElement(By.name("realname")).sendKeys("Demo User2");
		driver.findElement(By.name("email")).sendKeys("demo@gmail.com");
		driver.findElement(By.xpath("//input[@value='Create User']")).click();
		driver.findElement(By.xpath("//a[contains(text(),'Manage')]")).click();
		Thread.sleep(3000);
		AssertJUnit.assertEquals(driver.findElement(By.xpath("//a[text()='Demo User2']")).getText(),
				"Demo User2");
	}

	@AfterMethod
	public void close() {
		driver.quit();
	}

	public static void jsClick(WebElement element) {
		((JavascriptExecutor) driver).executeScript("arguments[0].click();", element);
	}

	public boolean isElementPresent(By by) {
		try {
			driver.findElement(by);
			return true;
		} catch (org.openqa.selenium.NoSuchElementException e) {
			return false;
		}
	}

}