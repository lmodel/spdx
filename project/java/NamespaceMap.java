package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A mapping between prefixes and namespace partial URIs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NamespaceMap  {

  private String prefix;
  private String namespace;

}