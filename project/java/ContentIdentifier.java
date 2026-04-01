package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A canonical, unique, immutable identifier
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContentIdentifier extends IntegrityMethod {

  private String contentIdentifierValue;
  private String contentIdentifierType;

}