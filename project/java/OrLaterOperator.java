package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Portion of an AnyLicenseInfo representing this version, or any later version,
of the indicated License.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrLaterOperator extends ExtendableLicense {

  private License subjectLicense;

}