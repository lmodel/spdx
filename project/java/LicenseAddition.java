package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Abstract class for additional text intended to be added to a License, but
which is not itself a standalone License.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class LicenseAddition extends Element {

  private String standardAdditionTemplate;
  private List<String> seeAlso;
  private String obsoletedBy;
  private String licenseXml;
  private boolean isDeprecatedAdditionId;
  private String additionText;

}