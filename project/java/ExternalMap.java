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
  A map of Element identifiers that are used within an SpdxDocument but defined external to that SpdxDocument.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalMap  {

  private URI type;
  private List<IntegrityMethod> verifiedUsing;
  private Artifact definingArtifact;
  private URI externalSpdxId;
  private URI locationHint;


}