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
  A collection of SPDX Elements that could potentially be serialized.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SpdxDocument extends ElementCollection {

  private AnyLicenseInfo dataLicense;
  private List<ExternalMap> import_;
  private List<NamespaceMap> namespaceMap;


}