package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Portion of an AnyLicenseInfo representing a set of licensing information
where all elements apply.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConjunctiveLicenseSet extends AnyLicenseInfo {

  private List<AnyLicenseInfo> member;

}