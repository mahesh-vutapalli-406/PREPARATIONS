Maven Cheat Sheet
=================

1\. Maven Basics
----------------

### Install Maven

-   Download from: [Apache Maven](https://maven.apache.org/download.cgi)
-   Verify installation:

    ```
    mvn -version

    ```

### Maven Workflow

1.  Create project: `mvn archetype:generate`
2.  Compile: `mvn compile`
3.  Package: `mvn package`
4.  Install: `mvn install`
5.  Deploy: `mvn deploy`

2\. Maven Commands
------------------

### Build & Lifecycle Commands

Maven has a predefined build lifecycle divided into phases:

#### 1\. **Clean Lifecycle**

-   `mvn pre-clean` -- Executes processes before cleaning
-   `mvn clean` -- Deletes target directory (removes compiled files)
-   `mvn post-clean` -- Executes processes after cleaning

#### 2\. **Default Lifecycle (Main Build Process)**

-   `mvn validate` -- Validates the project structure and checks the necessary information is available
-   `mvn compile` -- Compiles the source code of the project into bytecode
-   `mvn test` -- Runs unit tests using a testing framework such as JUnit
-   `mvn package` -- Packages compiled code and dependencies into a distributable format (JAR/WAR)
-   `mvn verify` -- Runs integration tests to check package validity before installation
-   `mvn install` -- Installs the package into the local repository (`~/.m2/repository`) for local development use
-   `mvn deploy` -- Copies the built package to a remote repository for sharing and collaboration

#### 3\. **Site Lifecycle**

-   `mvn site` -- Generates project documentation based on POM configuration
-   `mvn site:deploy` -- Publishes the generated site documentation to a specified server

### Dependency & Plugin Management

-   `mvn dependency:tree` -- Show dependency hierarchy to analyze conflicts
-   `mvn dependency:resolve` -- Resolve and download dependencies required for the project
-   `mvn help:effective-pom` -- Display the complete, final POM as used by Maven
-   `mvn help:describe -Dplugin=<plugin>` -- Describe details and goals of a specific Maven plugin

### Running Applications

-   `mvn exec:java -Dexec.mainClass=<main-class>` -- Run a Java application specified in the POM
-   `mvn spring-boot:run` -- Start a Spring Boot application

3\. Understanding POM.xml
-------------------------

### What is POM.xml?

-   Project Object Model (POM) is the core configuration file in Maven.

### POM.xml Structure

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0.0</version>
  <packaging>jar</packaging>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>2.6.3</version>
    </dependency>
  </dependencies>
</project>

```

### Explanation of Fields in POM.xml

-   `<modelVersion>` -- Defines POM version
-   `<groupId>` -- Unique identifier for a project group
-   `<artifactId>` -- Name of the project
-   `<version>` -- Project version
-   `<packaging>` -- Package type (jar, war, etc.)
-   `<dependencies>` -- List of project dependencies
-   `<build>` -- Build configurations, including plugins
-   `<repositories>` -- Custom repository locations for dependencies
-   `<properties>` -- Define custom properties and variables

4\. .m2 Directory
-----------------

-   Located at `~/.m2/` (Linux/macOS) or `C:\Users\<user>\.m2\` (Windows)
-   Stores:
    -   Local repository (`repository/` folder) containing downloaded dependencies and installed artifacts
    -   Settings (`settings.xml` file) containing configuration details for Maven execution

5\. settings.xml File
---------------------

-   Configures Maven behavior
-   Located in `~/.m2/settings.xml`

### Example settings.xml

```
<settings>
  <mirrors>
    <mirror>
      <id>central-mirror</id>
      <mirrorOf>central</mirrorOf>
      <url>https://repo.maven.apache.org/maven2</url>
      <layout>default</layout>
    </mirror>
  </mirrors>
</settings>

```

### Explanation

-   `<mirrors>` -- Defines repository mirrors to optimize dependency downloads
-   `<servers>` -- Authentication details for accessing secured repositories
-   `<profiles>` -- Configuration profiles for different environments (e.g., dev, test, prod)
-   `<activeProfiles>` -- Specifies which profile to activate by default

This Maven cheat sheet covers essential commands, lifecycle phases, POM structure, and configuration files.