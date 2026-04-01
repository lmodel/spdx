package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Provide context for a relationship that occurs in the lifecycle.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LifecycleScopedRelationship extends Relationship {

  private String scope;

}