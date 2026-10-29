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
  Abstract class for the portion of an AnyLicenseInfo representing a license.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class License extends ExtendableLicense {

  private String licenseText;
  private String licenseXml;
  private String obsoletedBy;
  private List<URI> seeAlso;
  private Boolean isDeprecatedLicenseId;
  private Boolean isFsfLibre;
  private Boolean isOsiApproved;
  private String standardLicenseHeader;
  private String standardLicenseTemplate;


}