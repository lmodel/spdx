package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Portion of an AnyLicenseInfo representing a License which has additional
text applied to it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WithAdditionOperator extends AnyLicenseInfo {

  private ExtendableLicense subjectExtendableLicense;
  private LicenseAddition subjectAddition;

}