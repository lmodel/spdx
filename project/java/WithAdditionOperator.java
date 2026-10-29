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
  Portion of an AnyLicenseInfo representing a License which has additional text applied to it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WithAdditionOperator extends AnyLicenseInfo {

  private LicenseAddition subjectAddition;
  private ExtendableLicense subjectExtendableLicense;


}