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
  Portion of an AnyLicenseInfo representing a set of licensing information where only one of the elements applies.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DisjunctiveLicenseSet extends AnyLicenseInfo {

  private List<AnyLicenseInfo> member;


}