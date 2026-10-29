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
  Abstract class for additional text intended to be added to a License, but which is not itself a standalone License.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class LicenseAddition extends Element {

  private String licenseXml;
  private String obsoletedBy;
  private List<URI> seeAlso;
  private String additionText;
  private Boolean isDeprecatedAdditionId;
  private String standardAdditionTemplate;


}