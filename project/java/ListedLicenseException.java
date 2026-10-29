package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A license exception that is listed on the SPDX Exceptions list.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListedLicenseException extends LicenseAddition {

  private String deprecatedVersion;
  private String listVersionAdded;


}