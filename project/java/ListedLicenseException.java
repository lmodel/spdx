package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A license exception that is listed on the SPDX Exceptions list.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ListedLicenseException extends LicenseAddition {

  private String listVersionAdded;
  private String deprecatedVersion;

}