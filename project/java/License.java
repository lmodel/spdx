package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Abstract class for the portion of an AnyLicenseInfo representing a license.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class License extends ExtendableLicense {

  private String obsoletedBy;
  private String standardLicenseHeader;
  private List<String> seeAlso;
  private boolean isFsfLibre;
  private boolean isDeprecatedLicenseId;
  private boolean isOsiApproved;
  private String licenseXml;
  private String licenseText;
  private String standardLicenseTemplate;

}