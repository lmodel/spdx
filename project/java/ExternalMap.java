package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A map of Element identifiers that are used within an SpdxDocument but defined
external to that SpdxDocument.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExternalMap  {

  private Artifact definingArtifact;
  private String locationHint;
  private String externalSpdxId;
  private List<IntegrityMethod> verifiedUsing;

}