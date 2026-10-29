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
  An SPDX Element containing an SPDX license expression string.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LicenseExpression extends AnyLicenseInfo {

  private List<DictionaryEntry> customIdToUri;
  private String licenseExpression;
  private String licenseListVersion;


}